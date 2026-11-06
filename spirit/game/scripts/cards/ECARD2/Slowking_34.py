from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import bursting_hand, shuffle_attack


card = PokemonCardDef(
    guid="b884dad7-145f-5e1d-aa50-dee615ea159c",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowking.Name",
    display_name="Slowking",
    searchable_by=["Slowking", "Stage 1", "Slowking"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Attack(
            title="Bursting Hand",
            game_text="Look at your opponent's hand. This attack does 10 damage times the number of Energy cards there.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=bursting_hand,
        ),
        Attack(
            title="Shuffle Attack",
            game_text="Look at a number of cards on top of your opponent's deck equal to the number of Energy cards attached to the Defending Pok\u00e9mon. Put those cards in any order, and then put them back on top of your opponent's deck.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=shuffle_attack,
        ),
    ],
)
