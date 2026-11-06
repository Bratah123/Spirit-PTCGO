from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ecard import searchlight


card = PokemonCardDef(
    guid="3de6417d-441b-5d61-b849-261608bbcf7e",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightLanturn.Name",
    display_name="Light Lanturn",
    searchable_by=["Light Lanturn", "Stage 1", "LightLanturn"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    family_id=171,
    abilities=[
        Attack(
            title="Searchlight",
            game_text="Flip a coin. If heads, each player may choose a card from his or her discard pile and put it into his or her hand.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=searchlight,
        ),
        Attack(
            title="Spark",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose 1 of them and this attack does 10 damage to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
            effect=snipe_attack(10, also_base=True),
        ),
    ],
)
