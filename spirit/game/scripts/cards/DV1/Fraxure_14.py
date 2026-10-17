from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import (
    AttrID, PokemonTypes, PokemonStage, Rarities, AbilityTypes,
)
from spirit.game.session.passives import Passive


class GritPassive(Passive):
    """If this Pokémon has a Special Condition, its attacks do +40."""

    def modify_damage_dealt(self, calc, carrier):
        if calc.attacker is not carrier:
            return
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        if not (carrier.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
            return
        calc.amount += 40


card = PokemonCardDef(
    guid="3665cf9c-4cff-543d-8917-f1693321f78c",
    key="DV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fraxure.Name",
    display_name="Fraxure",
    searchable_by=["Fraxure", "Stage 1", "Fraxure"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="DV1",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Axew.Name",
    family_id=610,
    abilities=[
        Ability(
            title="Grit",
            game_text="If this Pok\u00e9mon is affected by a Special Condition, each of its attacks does 40 more damage (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=GritPassive(),
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
