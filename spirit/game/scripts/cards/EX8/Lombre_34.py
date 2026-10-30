"""STUB: effect not implemented — do not guess mechanics.
Lombre (EX8 #34): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import blot_heal, natural_cure_on_water_attach


card = PokemonCardDef(
    guid="10e3b03f-bcb6-52ac-b8fd-08689012c6a0",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    display_name="Lombre",
    searchable_by=["Lombre", "Stage 1", "Lombre"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lotad.Name",
    family_id=270,
    abilities=[
        Ability(
            title="Natural Cure",
            game_text="When you attach a Water Energy card from your hand to Lombre, remove all Special Conditions from Lombre.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=natural_cure_on_water_attach(),
        ),
        Attack(
            title="Blot",
            game_text="Remove 2 damage counters from Lombre.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=blot_heal(),
        ),
    ],
)