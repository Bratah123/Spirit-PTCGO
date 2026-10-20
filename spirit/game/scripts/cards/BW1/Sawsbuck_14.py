from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="208a81a7-87e2-5662-933a-efaeca9845ca",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sawsbuck.Name",
    display_name="Sawsbuck",
    searchable_by=["Sawsbuck", "Stage 1", "Sawsbuck"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Deerling.Name",
    family_id=585,
    abilities=[
        Attack(
            title="Nature Power",
            game_text="Does 10 more damage for each Grass Energy attached to both your and your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per(
                count_energy("both", energy_type=PokemonTypes.GRASS), 10, base=20,
            ),
        ),
        Attack(
            title="Horn Leech",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=heal_attack(20),
        ),
    ],
)
