from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import gust_attack


card = PokemonCardDef(
    guid="b3f158b0-9cdb-52cb-80f0-b34f8d815e88",
    key="BASE2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victreebel.Name",
    display_name="Victreebel",
    searchable_by=["Victreebel", "Stage 2", "Victreebel"],
    subtypes=["Stage 2"],
    collector_number=30,
    set_code="BASE2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name",
    family_id=69,
    abilities=[
        Attack(
            title="Lure",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose 1 of them and switch it with his or her Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=gust_attack(),
        ),
        Attack(
            title="Acid",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon can't retreat during your next turn.",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
            effect=condition_attack(no_retreat=True, flip=True),
        ),
    ],
)
