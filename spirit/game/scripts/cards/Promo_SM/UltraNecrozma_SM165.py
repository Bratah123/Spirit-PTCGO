from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.smp import shining_burst

card = PokemonCardDef(
    guid="ca47c5aa-e8d1-565f-b61d-b7c20fabca70",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UltraNecrozma.Name",
    display_name="Ultra Necrozma",
    searchable_by=["Ultra Necrozma", "Basic", "Ultra Beast", "UltraNecrozma"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=165,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=800,
    abilities=[
        Attack(
            title="Shining Burst",
            game_text="If the total of both players' remaining Prize cards is 6 or less, discard all Energy attached to this Pok\u00e9mon, and this attack does 100 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.METAL: 2},
            damage=100,
            damage_operator="+",
            effect=shining_burst,
        ),
    ],
)