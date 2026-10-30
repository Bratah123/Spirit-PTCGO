"""STUB: effect not implemented — do not guess mechanics.
Metang (EX5 #44): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.ex import levitate_any_energy_passive

card = PokemonCardDef(
    guid="7f8d32fc-efeb-54fe-b5e5-dfd14b0a204f",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    display_name="Metang",
    searchable_by=["Metang", "Stage 1", "Metang"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    family_id=374,
    abilities=[
        Ability(
            title="Levitate",
            game_text="If Metang has any Energy attached to it, Metang's Retreat Cost is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=levitate_any_energy_passive(),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)