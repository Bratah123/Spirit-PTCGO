from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if

card = PokemonCardDef(
    guid="4ff36885-2d95-57cd-a596-e9890ab209d3",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianArcanine.Name",
    display_name="Hisuian Arcanine",
    searchable_by=["Hisuian Arcanine", "Stage 1", "HisuianArcanine"],
    subtypes=["Stage 1"],
    collector_number=84,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianGrowlithe.Name",
    family_id=58,
    abilities=[
        Attack(
            title="Very Vulnerable",
            game_text="If you have no cards in your hand, this attack does 150 more damage.",
            cost={},
            damage=10,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.hand_size() == 0, 150, base=10),
        ),
        Attack(
            title="Sharp Fang",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)