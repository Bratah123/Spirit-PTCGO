from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import big_eggsplosion, psychic_exchange

card = PokemonCardDef(
    guid="7119b7a7-9378-59ef-9088-4aebc37724a1",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name",
    display_name="Exeggutor",
    searchable_by=["Exeggutor", "Stage 1", "Exeggutor"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="EX6",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Psychic Exchange",
            game_text="Shuffle your hand into your deck. Draw up to 8 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=psychic_exchange(8),
        ),
        Attack(
            title="Big Eggsplosion",
            game_text="Flip a coin for each Energy attached to Exeggutor. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=big_eggsplosion(40),
        ),
    ],
)