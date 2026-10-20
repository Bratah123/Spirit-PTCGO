from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6af9859d-7d35-5c1d-b1ee-009821ab4557",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TornadusEX.Name",
    display_name="Tornadus-EX",
    searchable_by=["Tornadus-EX", "Basic", "EX", "Team Plasma", "TornadusEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=98,
    set_code="BW9",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=641,
    abilities=[
        Attack(
            title="Windfall",
            game_text="Shuffle your hand into your deck. Then, draw 6 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Jet Blast",
            game_text="This attack does 30 more damage for each Plasma Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)