from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.passives_common import is_in_active_spot, opposing_active
from spirit.game.session.passives import Passive


class StrangleholdMasterPassive(Passive):
    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if is_in_active_spot(carrier) and opposing_active(pokemon, carrier):
            return cost + 2
        return cost


def _same_hand_size(ctx):
    return ctx.hand_size(ctx.player_id) == ctx.hand_size(ctx.opponent_id)


card = PokemonCardDef(
    guid="e62bc2c7-139b-5741-b864-43ed029d1cab",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grapploct.Name",
    display_name="Grapploct",
    searchable_by=["Grapploct", "Stage 1", "Grapploct"],
    subtypes=["Stage 1"],
    collector_number=92,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clobbopus.Name",
    family_id=852,
    abilities=[
        Ability(
            title="Stranglehold Master",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent's Active Pok\u00e9mon's Retreat Cost is ColorlessColorless more.",
            passive=StrangleholdMasterPassive(),
        ),
        Attack(
            title="Synchro Buster",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 80 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=bonus_if(_same_hand_size, 80),
        ),
    ],
)