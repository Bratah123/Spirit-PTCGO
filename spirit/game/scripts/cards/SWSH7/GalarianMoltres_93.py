from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="55dce45d-bc5d-5ae3-993d-143d6bb8a1c0",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMoltres.Name",
    display_name="Galarian Moltres",
    searchable_by=["Galarian Moltres", "Basic", "GalarianMoltres"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=146,
    abilities=[
        Ability(
            title="Malevolent Charge",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may attach up to 2 Darkness Energy cards from your hand to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Fiery Wrath",
            game_text="This attack does 50 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)