from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="85361b1b-0949-5f0f-9a33-53d03e351d18",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mismagius.Name",
    display_name="Mismagius",
    searchable_by=["Mismagius", "Stage 1", "Mismagius"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="BW11",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name",
    family_id=200,
    abilities=[
        Attack(
            title="Absorb Life",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=heal_attack(10),
        ),
        Attack(
            title="Spooky Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)