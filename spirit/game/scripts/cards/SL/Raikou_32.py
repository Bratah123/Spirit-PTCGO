"""STUB: effect not implemented — do not guess mechanics.
Raikou (SL #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sl import is_basic_lightning_energy, is_benched
from spirit.game.card_effects.support_common import attach_from_discard

card = PokemonCardDef(
    guid="75766f80-cf52-5dc2-9845-52a3f166b5b7",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raikou.Name",
    display_name="Raikou",
    searchable_by=["Raikou", "Basic", "Raikou"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="SL",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=243,
    abilities=[
        Attack(
            title="Booming Thunder",
            game_text="Attach a Lightning Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=attach_from_discard(
                is_basic_lightning_energy, count=1, target=is_benched,
                prompt="Choose a Lightning Energy card to attach",
            ),
        ),
        Attack(
            title="Electric Ball",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
        ),
    ],
)