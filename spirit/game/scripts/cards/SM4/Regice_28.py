from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm4 import IcebergShieldPassive

card = PokemonCardDef(
    guid="13cd7e74-c8be-5b36-aa42-f687a828c644",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regice.Name",
    display_name="Regice",
    searchable_by=["Regice", "Basic", "Regice"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="SM4",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=378,
    abilities=[
        Ability(
            title="Iceberg Shield",
            game_text="If you have Regirock in play, prevent all effects of attacks, including damage, done to this Pok\u00e9mon by your opponent's Stage 2 Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=IcebergShieldPassive(),
        ),
        Attack(
            title="Frost Smash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)