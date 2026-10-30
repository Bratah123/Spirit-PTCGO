"""STUB: effect not implemented — do not guess mechanics.
Natu (EX8 #66): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.ex import mirror_coat_reflect_burn_poison



card = PokemonCardDef(
    guid="6ada6605-b16b-5869-8d9f-d25e6c62d37e",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    display_name="Natu",
    searchable_by=["Natu", "Basic", "Natu"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="EX8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=177,
    abilities=[
        Ability(
            title="Mirror Coat",
            game_text="If Natu is Burned or Poisoned by an opponent's attack (even if Natu is Knocked Out), the Attacking Pok\u00e9mon is now affected by the same Special Conditions (1 if there is only 1).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=mirror_coat_reflect_burn_poison(),
        ),
        Attack(
            title="Razor Wind",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=flip_or_nothing(),
        ),
    ],
)