from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import bonfire


card = PokemonCardDef(
    guid="a51fea12-7946-5bf2-b07f-4a652005f52e",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesCharmeleon.Name",
    display_name="Blaine's Charmeleon",
    searchable_by=["Blaine's Charmeleon", "Stage 1", "BlainesCharmeleon"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesCharmander.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Fire Claws",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
        ),
        Attack(
            title="Bonfire",
            game_text="Flip 3 coins. For each heads, discard 1 Fire Energy card attached to Blaine's Charmeleon. If you can't discard Energy cards, this attack does nothing. This attack does 10 damage times the number of heads to each of your opponent's Pok\u00e9mon. Don't apply Weakness and Resistance for this attack. (Any other effects that would happen after applying Weakness and Resistance still happen.)",
            cost={PokemonTypes.FIRE: 3},
            effect=bonfire,
        ),
    ],
)
