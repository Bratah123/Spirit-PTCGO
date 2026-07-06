from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e35c2272-428c-5c09-a29e-f112deb739f9",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rowlet.Name",
    display_name="Rowlet",
    searchable_by=["Rowlet", "Basic", "Rowlet"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=722,
    abilities=[
        Ability(
            title="Sky Circus",
            game_text="If you played Bird Keeper from your hand during this turn, ignore all Energy in this Pok\u00e9mon's attack costs.",
            effect=unimplemented,
        ),
        Attack(
            title="Wind Shard",
            game_text="This attack does 60 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=unimplemented,
        ),
    ],
)