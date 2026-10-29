from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.sm7 import (
    beat_up,
)


card = PokemonCardDef(
    guid="c575fe06-dce3-540c-9867-dc5e48cf4f51",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    display_name="Sneasel",
    searchable_by=["Sneasel", "Basic", "Sneasel"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="SM7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=215,
    abilities=[
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=3, per_heads=10),
        ),
        Attack(
            title="Beat Up",
            game_text="Flip a coin for each Pok\u00e9mon you have in play. This attack does 30 damage for each heads.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=30,
            damage_operator="x",
            effect=beat_up,
        ),
    ],
)