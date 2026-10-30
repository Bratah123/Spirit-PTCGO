from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="32b6b8d0-3d90-5533-8c55-95a40ffa399e",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scytherex.Name",
    display_name="Scyther ex",
    searchable_by=["Scyther ex", "Basic", "ex", "Scytherex"],
    subtypes=["Basic", "ex"],
    collector_number=102,
    set_code="EX1",
    rarity=Rarities.RareHoloEX,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=123,
    abilities=[
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Scyther ex during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
