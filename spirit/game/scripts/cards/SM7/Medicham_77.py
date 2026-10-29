from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.sm7 import (
    strike_of_enlightenment,
)


card = PokemonCardDef(
    guid="8afd4280-bf03-5254-a077-01f4651ad80e",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Medicham.Name",
    display_name="Medicham",
    searchable_by=["Medicham", "Stage 1", "Medicham"],
    subtypes=["Stage 1"],
    collector_number=77,
    set_code="SM7",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    family_id=307,
    abilities=[
        Attack(
            title="Strike of Enlightenment",
            game_text="If this Pok\u00e9mon's remaining HP is 30 or less, this attack does 160 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=10,
            damage_operator="+",
            effect=strike_of_enlightenment,
        ),
        Attack(
            title="Spinning Kick",
            game_text="This Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=90,
            # STUB: attack effect not implemented
            effect=recoil_attack(30),
        ),
    ],
)