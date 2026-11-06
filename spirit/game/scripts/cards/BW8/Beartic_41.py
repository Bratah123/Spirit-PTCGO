from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on, mill_attack


card = PokemonCardDef(
    guid="1ca957b6-618d-5539-9a0a-57b8f5883575",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beartic.Name",
    display_name="Beartic",
    searchable_by=["Beartic", "Stage 1", "Team Plasma", "Beartic"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=41,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubchoo.Name",
    family_id=613,
    abilities=[
        Attack(
            title="Powerful Rage",
            game_text="Does 20 damage times the number of damage counters on this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=damage_per(damage_counters_on('self'), 20),
        ),
        Attack(
            title="Glacier Drop",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=mill_attack(1),
        ),
    ],
)