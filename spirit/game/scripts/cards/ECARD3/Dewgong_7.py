from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import crushing_ice, freeze_lock


card = PokemonCardDef(
    guid="7dbb0dea-f367-52a7-ae0a-301a59661e48",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewgong.Name",
    display_name="Dewgong",
    searchable_by=["Dewgong", "Stage 1", "Dewgong"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="ECARD3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name",
    family_id=86,
    abilities=[
        Attack(
            title="Freeze Lock",
            game_text="Flip a coin. If heads, your opponent can't attach Energy cards from his or her hand to his or her Active Pok\u00e9mon during his or her next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=freeze_lock,
        ),
        Attack(
            title="Crushing Ice",
            game_text="This attack does 40 damage plus 10 more damage for each Colorless Energy in the Defending Pok\u00e9mon's Retreat Cost. Damage is calculated using the Defending Pok\u00e9mon's Retreat Cost after applying effects to the Retreat Cost.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=crushing_ice,
        ),
    ],
)
