"""STUB: effect not implemented — do not guess mechanics.
Yveltal (SL #54): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sl import is_benched, is_basic_darkness_energy
from spirit.game.card_effects.support_common import attach_from_discard, switch_self_attack


card = PokemonCardDef(
    guid="ed79555b-d825-5b83-ae2c-7f79608ba8ae",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yveltal.Name",
    display_name="Yveltal",
    searchable_by=["Yveltal", "Basic", "Yveltal"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="SL",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=717,
    abilities=[
        Attack(
            title="Strafe",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=switch_self_attack(optional=True),
        ),
        Attack(
            title="Oblivion Wing",
            game_text="Attach a Darkness Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=attach_from_discard(
                is_basic_darkness_energy, count=1, target=is_benched,
                prompt="Choose a Darkness Energy card to attach",
            ),
        ),
    ],
)