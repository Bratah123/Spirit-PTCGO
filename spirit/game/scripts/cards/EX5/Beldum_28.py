"""STUB: effect not implemented — do not guess mechanics.
Beldum (EX5 #28): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.ex import levitate_any_energy_passive

card = PokemonCardDef(
    guid="ce19fe74-0520-54b6-8414-1df7e5c3232b",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    display_name="Beldum",
    searchable_by=["Beldum", "Basic", "Beldum"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=374,
    abilities=[
        Ability(
            title="Levitate",
            game_text="If Beldum has any Energy attached to it, Beldum's Retreat Cost is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=levitate_any_energy_passive(),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)