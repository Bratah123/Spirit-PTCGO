from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import crushing_lava, streaming_mantle


card = PokemonCardDef(
    guid="59b7cd56-6574-542c-ae12-01d29e809f2a",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magcargo.Name",
    display_name="Magcargo",
    searchable_by=["Magcargo", "Stage 1", "Magcargo"],
    subtypes=["Stage 1"],
    collector_number=167,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    abilities=[
        Ability(
            title="Streaming Mantle",
            game_text="When you play Magcargo from your hand to evolve your Active Pok\u00e9mon, you may discard the top 3 cards of your deck and and then shuffle 3 basic Energy cards from your discard pile into your deck. If you do, your opponent does the same.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_EVOLVE,
            effect=streaming_mantle,
        ),
        Attack(
            title="Crushing Lava",
            game_text="You may discard a Fire or Fighting basic Energy card attached to Magcargo. If you discard a Fire Energy card in this way, the Defending Pok\u00e9mon is now Burned. If you discard a Fighting Energy card in this way, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=crushing_lava,
        ),
    ],
)
