"""STUB: effect not implemented — do not guess mechanics.
Dodrio (EX9 #26): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="70292ce9-a24e-5f65-b7d0-5cd9a8b67aec",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dodrio.Name",
    display_name="Dodrio",
    searchable_by=["Dodrio", "Stage 1", "Dodrio"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name",
    family_id=84,
    abilities=[
        Attack(
            title="Smash Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Smash Turn",
            game_text="After your attack, you may switch Dodrio with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            # STUB: attack effect not implemented
            effect=switch_self_attack(optional=True),
        ),
    ],
)