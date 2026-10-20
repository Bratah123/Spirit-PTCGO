from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, damage_per, count_energy


card = PokemonCardDef(
    guid="14fba9ff-18b4-5219-aa2b-e286cec973fb",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delphox.Name",
    display_name="Delphox",
    searchable_by=["Delphox", "Stage 2", "Delphox"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="XY10",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name",
    family_id=653,
    abilities=[
        Attack(
            title="Flickering Flames",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Psystorm",
            game_text="This attack does 20 damage times the amount of Energy attached to all Pok\u00e9mon in play.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_energy('both'), 20),
        ),
    ],
)