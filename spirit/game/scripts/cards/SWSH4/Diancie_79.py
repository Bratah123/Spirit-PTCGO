from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a89e5e42-398b-5c49-ba16-a24d79af8079",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Diancie.Name",
    display_name="Diancie",
    searchable_by=["Diancie", "Basic", "Diancie"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="SWSH4",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=719,
    abilities=[
        Ability(
            title="Sparkle Veil",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, any damage done to your Pok\u00e9mon by an opponent's attack is reduced by 30 (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Sensitive Ray",
            game_text="If you played a Supporter card from your hand during this turn, this attack does 70 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)