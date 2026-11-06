from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="16988d9d-4ad0-5693-b0f5-47114142e16f",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sunflora.Name",
    display_name="Sunflora",
    searchable_by=["Sunflora", "Stage 1", "Sunflora"],
    subtypes=["Stage 1"],
    collector_number=105,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sunkern.Name",
    family_id=191,
    abilities=[
        Attack(
            title="Energy Plant",
            game_text="Search your deck for a basic Energy card and attach it to 1 of your Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=search_attach_energy(predicate=is_basic_energy_card),
        ),
        Attack(
            title="Trip Over",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 30 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)
