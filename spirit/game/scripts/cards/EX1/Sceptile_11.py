from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import lizard_poison


card = PokemonCardDef(
    guid="b7a7f4d8-9fab-51ce-9ee5-3db836cc9497",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sceptile.Name",
    display_name="Sceptile",
    searchable_by=["Sceptile", "Stage 2", "Sceptile"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="EX1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    family_id=252,
    abilities=[
        Attack(
            title="Lizard Poison",
            game_text="If 1 Energy is attached to Sceptile, the Defending Pok\u00e9mon is now Asleep. If 2 Energy is attached to Sceptile, the Defending Pok\u00e9mon is now Poisoned. If 3 Energy is attached to Sceptile, the Defending Pok\u00e9mon is now Asleep and Poisoned. If 4 or more Energy is attached to Sceptile, the Defending Pok\u00e9mon is now Asleep, Burned, and Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=lizard_poison(),
        ),
        Attack(
            title="Solarbeam",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)
