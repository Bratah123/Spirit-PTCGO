from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c033b410-8ffe-587e-9ff0-60d5858dbf6e",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TalonflameV.Name",
    display_name="Talonflame V",
    searchable_by=["Talonflame V", "Basic", "V", "TalonflameV"],
    subtypes=["Basic", "V"],
    collector_number=168,
    set_code="SWSH4",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=663,
    abilities=[
        Attack(
            title="Fast Flight",
            game_text="If you go first, you can use this attack during your first turn. Discard your hand and draw 6 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Bright Wing",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=unimplemented,
        ),
    ],
)