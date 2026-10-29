from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.sm7 import (
    surprising_pattern,
)


card = PokemonCardDef(
    guid="14cf6cc5-f0c3-5b26-8e82-58a213f3c7fe",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Masquerain.Name",
    display_name="Masquerain",
    searchable_by=["Masquerain", "Stage 1", "Masquerain"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name",
    family_id=283,
    abilities=[
        Attack(
            title="Surprising Pattern",
            game_text="Discard all Special Energy from each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=surprising_pattern,
        ),
        Attack(
            title="Hurricane Wing",
            game_text="Flip 4 coins. This attack does 40 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=4, per_heads=40),
        ),
    ],
)