from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="e3fc7fef-d5da-578f-a32d-9fab79851b47",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name",
    display_name="Quilava",
    searchable_by=["Quilava", "Stage 1", "Quilava"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cyndaquil.Name",
    family_id=155,
    abilities=[
        Attack(
            title="Hammer In",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Super Singe",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 3},
            damage=60,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
    ],
)