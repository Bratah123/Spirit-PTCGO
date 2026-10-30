"""STUB: effect not implemented — do not guess mechanics.
Xatu (EX8 #29): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import dazzle_dance_confuse, mirror_coat_reflect_burn_poison, psyloop_trainers


card = PokemonCardDef(
    guid="d4fad0fa-02cf-56ce-ab30-f6e9f879f929",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xatu.Name",
    display_name="Xatu",
    searchable_by=["Xatu", "Stage 1", "Xatu"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="EX8",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    family_id=177,
    abilities=[
        Ability(
            title="Mirror Coat",
            game_text="If Xatu is Burned or Poisoned by an opponent's attack (even if Xatu is Knocked Out), the Attacking Pok\u00e9mon is now affected by the same Special Conditions (1 if there is only 1).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=mirror_coat_reflect_burn_poison(),
        ),
        Attack(
            title="Dazzle Dance",
            game_text="Each Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=dazzle_dance_confuse(),
        ),
        Attack(
            title="Psyloop",
            game_text="Does 30 damage plus 30 more damage for each Trainer card your opponent has in play.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=psyloop_trainers(),
        ),
    ],
)