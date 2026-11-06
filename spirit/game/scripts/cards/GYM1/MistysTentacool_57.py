from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import crystal_beam


card = PokemonCardDef(
    guid="85fd551b-2b87-5bde-a43c-a8eaad784c4d",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysTentacool.Name",
    display_name="Misty's Tentacool",
    searchable_by=["Misty's Tentacool", "Basic", "MistysTentacool"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=72,
    abilities=[
        Attack(
            title="Crystal Beam",
            game_text="Flip a coin. If heads, your opponent can't attach Energy cards to the Defending Pok\u00e9mon during his or her next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=crystal_beam,
        ),
    ],
)
