from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_in_play, damage_per
from spirit.game.card_effects.ecard import flip_heal_one, pokemon_name_contains


card = PokemonCardDef(
    guid="ba941264-7c25-58fb-9034-e1a945713831",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bellossom.Name",
    display_name="Bellossom",
    searchable_by=["Bellossom", "Stage 2", "Bellossom"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="NEO1",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Attack(
            title="Sweet Nectar",
            game_text="Flip a coin. If heads, remove all damage counters from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=flip_heal_one(all_damage=True),
        ),
        Attack(
            title="Flower Dance",
            game_text="Does 30 damage times the number of cards with Bellossom in their names that you have in play (including this one).",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=damage_per(
                count_in_play("mine", pokemon_name_contains("Bellossom")), 30),
        ),
    ],
)
