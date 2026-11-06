from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage


card = PokemonCardDef(
    guid="6d63f89b-5dd8-5897-9090-4c201aa6ca6f",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Qwilfish.Name",
    display_name="Qwilfish",
    searchable_by=["Qwilfish", "Basic", "Qwilfish"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="NEO3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=211,
    abilities=[
        Attack(
            title="Poison Sting",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
        Attack(
            title="Needle Storm",
            game_text="Flip a coin until you get tails. This attack does 20 damage times the number of heads you get.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage(until_tails=True, per_heads=20),
        ),
    ],
)
