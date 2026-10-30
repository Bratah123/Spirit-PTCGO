from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import damage_all_unmodified


card = PokemonCardDef(
    guid="f13daad2-c480-593e-9343-0eacef41f886",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksGolbat.Name",
    display_name="Brock's Golbat",
    searchable_by=["Brock's Golbat", "Stage 1", "BrocksGolbat"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksZubat.Name",
    family_id=41,
    abilities=[
        Attack(
            title="Dive",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Spiral Dive",
            game_text="Does 10 damage to each of your opponent's Pok\u00e9mon. Don't apply Weakness and Resistance.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=damage_all_unmodified(10),
        ),
    ],
)
