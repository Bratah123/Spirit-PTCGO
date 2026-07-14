from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if


def _entered_active_this_turn(ctx):
    return ctx.entered_active_this_turn(ctx.attacker)


card = PokemonCardDef(
    guid="c5904577-7950-5bbb-b720-30dc82474c01",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golisopod.Name",
    display_name="Golisopod",
    searchable_by=["Golisopod", "Stage 1", "Golisopod"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="PGO",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    family_id=767,
    abilities=[
        Attack(
            title="First Impression",
            game_text="If this Pok\u00e9mon moved from your Bench to the Active Spot this turn, this attack does 90 more damage.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(_entered_active_this_turn, 90),
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)