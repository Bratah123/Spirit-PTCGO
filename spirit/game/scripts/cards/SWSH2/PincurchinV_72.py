from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c9f867cb-26f1-5185-8507-ba06380a14f0",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PincurchinV.Name",
    display_name="Pincurchin V",
    searchable_by=["Pincurchin V", "Basic", "V", "PincurchinV"],
    subtypes=["Basic", "V"],
    collector_number=72,
    set_code="SWSH2",
    rarity=Rarities.RareHoloV,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=871,
    abilities=[
        Ability(
            title="Counterattack Kerzap",
            game_text="If this Pok\u00e9mon is in the Active Spot and is damaged by an opponent's attack (even if it is Knocked Out), flip 3 coins. For each heads, put 3 damage counters on the Attacking Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Sparking Strike",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)