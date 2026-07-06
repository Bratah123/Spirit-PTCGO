from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ed9b3c3f-481f-58a4-820d-a5bb1b71d843",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CramorantV.Name",
    display_name="Cramorant V",
    searchable_by=["Cramorant V", "Basic", "V", "CramorantV"],
    subtypes=["Basic", "V"],
    collector_number=198,
    set_code="SWSH1",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=845,
    abilities=[
        Attack(
            title="Beak Catch",
            game_text="Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Spit Shot",
            game_text="Discard all Energy from this Pok\u00e9mon. This attack does 160 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=unimplemented,
        ),
    ],
)