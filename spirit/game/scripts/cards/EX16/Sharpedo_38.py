"""STUB: effect not implemented — do not guess mechanics.
Sharpedo (EX16 #38): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import darkness_charge_self
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="4b6f42fa-2d49-547a-a036-ee4475fb5526",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sharpedo.Name",
    display_name="Sharpedo",
    searchable_by=["Sharpedo", "Stage 1", "Sharpedo"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name",
    family_id=318,
    abilities=[
        Attack(
            title="Tight Jaw",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Darkness Charge",
            game_text="Put 1 damage counter on Sharpedo.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=darkness_charge_self(),
        ),
    ],
)