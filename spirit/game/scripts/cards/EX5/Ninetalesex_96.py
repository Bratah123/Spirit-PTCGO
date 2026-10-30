"""STUB: effect not implemented — do not guess mechanics.
Ninetales ex (EX5 #96): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.ex import fire_blast_discard, intense_glare

card = PokemonCardDef(
    guid="e7b30d72-d3d4-58aa-97db-b0aa73e59093",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetalesex.Name",
    display_name="Ninetales ex",
    searchable_by=["Ninetales ex", "Stage 1", "ex", "Ninetalesex"],
    subtypes=["Stage 1", "ex"],
    collector_number=96,
    set_code="EX5",
    rarity=Rarities.RareHoloEX,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Intense Glare",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with 1 of the Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch. The new Defending Pok\u00e9mon is now Burned and Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=intense_glare(),
        ),
        Attack(
            title="Fire Blast",
            game_text="Discard a Fire Energy attached to Ninetales ex.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=fire_blast_discard(),
        ),
    ],
)