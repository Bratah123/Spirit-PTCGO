from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

zen_shot = snipe_attack(60, pool=lambda p: is_pokemon_v(p.archetype_id), count=1,
                         prompt="Choose 1 of your opponent's Pokémon V")

card = PokemonCardDef(
    guid="8a0de134-d2ab-5cd5-bf34-0c539c9450a3",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EspeonV.Name",
    display_name="Espeon V",
    searchable_by=["Espeon V", "Basic", "V", "EspeonV"],
    subtypes=["Basic", "V"],
    collector_number=179,
    set_code="SWSH7",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=196,
    abilities=[
        Attack(
            title="Zen Shot",
            game_text="This attack does 60 damage to 1 of your opponent's Pok\u00e9mon V. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=zen_shot,
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)