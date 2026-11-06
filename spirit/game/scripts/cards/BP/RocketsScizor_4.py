from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import boost_own_next_turn, flip_protection


card = PokemonCardDef(
    guid="f9c226a5-6403-538a-8247-11e28eae0ad5",
    key="BP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsScizor.Name",
    display_name="Rocket's Scizor",
    searchable_by=["Rocket's Scizor", "Basic", "RocketsScizor"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="BP",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=212,
    abilities=[
        Attack(
            title="Focus",
            game_text="During your next turn, Rocket's Scizor's Agility attack's damage is doubled.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=boost_own_next_turn(20, attack_title="Agility"),
        ),
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Rocket's Scizor.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=flip_protection(prevent=True, effects_too=True),
        ),
    ],
)
