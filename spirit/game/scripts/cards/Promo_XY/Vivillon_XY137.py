from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, damage_per, count_energy


card = PokemonCardDef(
    guid="bee74dfa-3e5a-5857-9db8-eb294ecead8b",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vivillon.Name",
    display_name="Vivillon",
    searchable_by=["Vivillon", "Stage 2", "Vivillon"],
    subtypes=["Stage 2"],
    collector_number=137,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name",
    family_id=666,
    abilities=[
        Attack(
            title="Dizzying Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.CONFUSED, SpecialConditions.POISONED),
        ),
        Attack(
            title="Powder",
            game_text="This attack does 30 more damage for each Fire Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_energy('defender', energy_type=PokemonTypes.FIRE), 30, base=30),
        ),
    ],
)