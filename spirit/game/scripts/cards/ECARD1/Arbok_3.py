from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, condition_bonus_attack


card = PokemonCardDef(
    guid="639df36f-87b4-5163-b881-0821346d136f",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arbok.Name",
    display_name="Arbok",
    searchable_by=["Arbok", "Stage 1", "Arbok"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name",
    family_id=23,
    abilities=[
        Attack(
            title="Poison Spray",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Poison Reaction",
            game_text="If the Defending Pok\u00e9mon is Poisoned, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=condition_bonus_attack(20, SpecialConditions.POISONED),
        ),
    ],
)
