from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="55c4d099-7bd3-53d3-9efd-95a230a2b152",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stunfisk.Name",
    display_name="Stunfisk",
    searchable_by=["Stunfisk", "Basic", "Stunfisk"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="BW3",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=618,
    abilities=[
        Attack(
            title="Mud Shot",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Thunder",
            game_text="Flip a coin. If tails, this Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=flip_damage(coins=1, base=60, tails_self_damage=30),
        ),
    ],
)
