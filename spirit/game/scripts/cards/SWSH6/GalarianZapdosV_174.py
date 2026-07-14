from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack
from spirit.game.session.passives import Passive


class FightingInstinctPassive(Passive):
    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        owner = carrier.owning_player_id
        opponent = next((pid for pid in board.player_ids if pid != owner), None)
        if opponent is None or "Colorless" not in cost:
            return cost
        discount = sum(
            1 for p in board.pokemon_in_play(opponent) if is_pokemon_v(p.archetype_id)
        )
        if discount <= 0:
            return cost
        remaining = cost["Colorless"] - discount
        if remaining > 0:
            cost["Colorless"] = remaining
        else:
            del cost["Colorless"]
        return cost


card = PokemonCardDef(
    guid="99391ac2-9439-531d-8e43-9ff88d19e5c9",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianZapdosV.Name",
    display_name="Galarian Zapdos V",
    searchable_by=["Galarian Zapdos V", "Basic", "V", "GalarianZapdosV"],
    subtypes=["Basic", "V"],
    collector_number=174,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=145,
    abilities=[
        Ability(
            title="Fighting Instinct",
            game_text="This Pok\u00e9mon's attacks cost Colorless less for each of your opponent's Pok\u00e9mon V in play.",
            passive=FightingInstinctPassive(),
        ),
        Attack(
            title="Thunderous Kick",
            game_text="Before doing damage, discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=170,
            effect=discard_opponent_energy_attack(special_only=True, after_damage=False),
        ),
    ],
)