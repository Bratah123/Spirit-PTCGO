from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import HeavyweightPassive, burning_sludge


card = PokemonCardDef(
    guid="7fdb29da-30d3-5e60-b9ef-5d5e92e38dfa",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name",
    display_name="Muk",
    searchable_by=["Muk", "Stage 1", "Muk"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Heavyweight",
            game_text="As long as there is a Grass Energy attached to Muk, you must pay an additional ColorlessColorless to retreat it.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=HeavyweightPassive(),
        ),
        Attack(
            title="Burning Sludge",
            game_text="Flip a number of coins equal to the amount of Grass Energy attached to Muk. If any of them are heads, the Defending Pok\u00e9mon is now Poisoned and Burned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=burning_sludge,
        ),
    ],
)
