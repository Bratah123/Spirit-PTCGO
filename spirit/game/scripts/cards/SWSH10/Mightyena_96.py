from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.pokemon import is_pokemon_vmax
from spirit.game.session.passives import Passive, carrier_pokemon


class HustleBarkPassive(Passive):
    """If the opponent has any Pokemon VMAX in play, this Pokemon's attacks
    cost [C][C][C] less."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        opponent = next((p for p in board.player_ids
                          if p != carrier.owning_player_id), None)
        if opponent is None or "Colorless" not in cost:
            return cost
        if not any(is_pokemon_vmax(p.archetype_id)
                   for p in board.pokemon_in_play(opponent)):
            return cost
        remaining = cost["Colorless"] - 3
        if remaining > 0:
            cost["Colorless"] = remaining
        else:
            del cost["Colorless"]
        return cost


card = PokemonCardDef(
    guid="719ef6ce-7bb8-527d-b401-7b4db84e19ca",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mightyena.Name",
    display_name="Mightyena",
    searchable_by=["Mightyena", "Stage 1", "Mightyena"],
    subtypes=["Stage 1"],
    collector_number=96,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poochyena.Name",
    family_id=261,
    abilities=[
        Ability(
            title="Hustle Bark",
            game_text="If your opponent has any Pokémon VMAX in play, this Pokémon's attacks cost ColorlessColorlessColorless less.",
            passive=HustleBarkPassive(),
        ),
        Attack(
            title="Wild Tackle",
            game_text="This Pokémon also does 50 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=recoil_attack(50),
        ),
    ],
)
