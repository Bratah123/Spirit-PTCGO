from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="d1a3148a-2c6f-595d-8d38-7ffb3a0394da",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hippopotas.Name",
    display_name="Hippopotas",
    searchable_by=["Hippopotas", "Basic", "Hippopotas"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="BW4",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    family_id=449,
    abilities=[
        Attack(
            title="Sand Jet",
            game_text="Does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            effect=snipe_attack(20),
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)