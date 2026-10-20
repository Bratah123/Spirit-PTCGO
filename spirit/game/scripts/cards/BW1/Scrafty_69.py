from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="27c8a96a-641f-5779-85ee-9cc23a200cc2",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scrafty.Name",
    display_name="Scrafty",
    searchable_by=["Scrafty", "Stage 1", "Scrafty"],
    subtypes=["Stage 1"],
    collector_number=69,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    family_id=559,
    abilities=[
        Attack(
            title="Spit Acid",
            game_text="The Defending Pok\u00e9mon is now Burned. Flip a coin. If heads, the Defending Pok\u00e9mon is also Paralyzed.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=condition_attack(
                SpecialConditions.PARALYZED, flip=True,
                always_conditions=(SpecialConditions.BURNED,),
            ),
        ),
        Attack(
            title="High Jump Kick",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
